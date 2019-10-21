
Codelab Chalice
===============

Sur AWS placez-vous de préférence sur la region eu-west-1 (Ireland)


Etape 1 : Préparation de l'infra AWS
------------------------------------

Sur AWS créez un bucket S3 exposant un site web statique

Préfére la région eu-west-1 (Irland)

- choisissez le service S3
- cliquez sur "Create Bucket"
- Donnez lui un nom (Nom unique dans le service S3 pour tous les utilisateur)
- Cliquez sur create
- Vous devez maintenant voir votre bucket dans la list. Cliquez sur son nom pour l'ouvrir
- Allez dans l'onglet "Properties" et cliquez sur "Static website hosting"
- Sélectionnez "Use this bucket to host a website"
- Tapez "index.html" dans le champ "index document" et sauvez
- allez dans l'onglet "Permissions" et cliquez sur "Bucket Policy"
- Inserez dans le champ texte la policy suivante en changeant *<BUCKET_NAME>* par le nom de votre bucket
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<BUCKET_NAME>/*"
            }
        ]
    }
    ```

Les fichiers déposés sur votre bucket S3 seront maintenant disponible via l'url
https://<BUCKET_NAME>.s3-eu-west-1.amazonaws.com/<FILE_KEY>


Etape 2 : Configuration de l'app
--------------------------------

dans le fichier config.json
- Mettez à jour la varaibales d'environnement *IDENTITY*. Elle permetera d'identifier vous message dans Slack
- Déclarez une variable d'environnement *SLACK_MESSAGE_WH* au niveau du stage *dev* portant comme valeur l'url du webhook slack du channel choisi
- Déclarez une variable d'environnement *BUCKET_NAME* au niveau du stage *dev*


Etape 3 : Utilisation de sous-module et de Blueprints
-----------------------------------------------------

- Activez les blueprints dans app
- déclarez un blueprint "slack" dans le module chalicelib.slack et enregistrez le dans l'app


Etape 4 : Ajout des déclencheurs Chalice
----------------------------------------

- Sur la lambda *rocker_speak* ajouter un scheduler
- Sur la lambda *rock_on_stage* ajouter un trigger sur creation d'objet dans le bucket S3 *BUCKET_NAME*

Etape 5 : Déployer
------------------

A ce niveau vous pouvez déployer via la commande
```shell
chalice deploy
```
Selon la fréquence de votre planification des messages doivent apparaitre dans Slack

Ajoutez une image dans votre bucket S3.
En consultant les logs via la commande
```shell
chalice logs --name rock_on_stage --stage dev
```
Vous devez pouvoir voir que la lambda s'est déclenchée ainsi que le message slack généré

Etape 5 : Activation de Rekognition
-----------------------------------

- appelez la function analyse du module chalicelib.rekognition
- déployez, postez une image et consultez les logs

Une erreur dc'est produite indiquant un problème de droit pour l'utilisation du service rekognition

Etape 6 : Policy personalisée
-----------------------------

- Créez un fichier *policy-dev.json* dans le répertoire *.chalice* avec le contenu suivant :
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:*:*:*",
                "Effect": "Allow"
            },
            {
                "Action": [
                    "rekognition:DetectLabels",
                    "rekognition:StartLabelDetection",
                    "rekognition:GetLabelDetection"
                ],
                "Resource": "*",
                "Effect": "Allow"
            },
            {
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": "arn:aws:s3:::<BUCKET_NAME>*",
                "Effect": "Allow"
            }
        ]
    }
    ```

- indiquez que la lambda *rocker_on_stage* utilise une policy personalisée via la clé "autogen_policy" positionnée à false

- redéployez et testez


