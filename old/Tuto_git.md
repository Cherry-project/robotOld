# Instruction Git

Tout d'abord, si vous n'avez pas les droits en écriture, il vous faut forker le projet.
Ensuite, lorsque vous dévellopez une nouvelle fonctinnalité ou des corrections, il faudra alors faire une pull request afin que quelqu'un qui possède les droits en écriture les valides.

## Forker un projet

Pour forker un projet, une méthode simple est d'aller sur la page github du projet, et ensuite cliquer sur le bouton fork en haut à droite de la page. Github se charge du reste, et vous pourrez ensuite cloner votre répertoire créé sur votre compte, où vous avez alors les droits en écriture.

## Faire une pull request

Attention, ne faites une pull request seulement lorsque vous vous êtes assuré que la fonctionnalité fonctionne bien et n'impacte pas sur le code déjà existant.
Pour faire une pull request, il faut allez sur la page github de votre répertoire (celui sur votre compte, où vous avez les droits en écriture), et ensuite cliquer sur la bouton de la pull request. Vérifiez une dernière fois qu'il n'y a pas d'erreur puis soumettez la. 

## Les branches

A chaque nouvelle fonctionnalité, si vos modifications vons prendre plus d'un commit, il vous faut travailler dans une branche. Ainsi, vous pourrez dévelloper plusieurs fonctionnalité en même temps. De plus, cela permet une meilleur visibilité sur l'évolution du code.

### Création d'une branche

Voici par exemple, la création d'une branche pour la fonctionnalité X :

`git branch X`

Vous pouvez ainsi voir en tapant `git branch` que la branche a été créée, mais vous êtes encore sur la branche master (la branche courante est symbolisé par *).

`git checkout X` pour passer à la branche X (vérifier avec `git branch`)

Vous pouvez ensuite faire plusieurs modification sans impacter la branch master.

### Fusion de banches

Ensuite, quand votre fonctonnalité est fini et que vous voulez mettre ces modification sur la branche principale (master), il faut suivre ces étapes :

Se mettre dans la branch master : `git checkout master`, pour ensuite lancer le merge : `git merge X`

Todo : Mettre les différents cas (fast-forward ou récursif), et la résolution des conflits.

### Suppresion de branches

Pour supprimer une branche : `git branch -d X`. Si vous avez déjà fusionné la branche, il n'y aura pas de problème.
Si vous devez supprimer une branche non fusionnée, et ainsi perdre tout le travail réalisé dans la branche, il suffit de faire `git branch -D X`.

### Branches distantes
Pour l'instant, toute vos branches sont locales, et n'apparaissent pas sur github.

Pour résoudre ce problème, lors de la création d'une branche, il faut faire en plus la commande `git push origin X`, en étant dans la branch X.

Et pour la supprimer, avant de la supprimer localement, il faut faire `git push origin :X`

Enfin, pour récuperer une branche distantes, il faut faire `git branch X origin/X`