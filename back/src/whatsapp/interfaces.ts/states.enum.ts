export enum States {
  // Estado inicial al no estar registrado
  START = "START",

  // Proceso de registro
  REGISTER_USER = "REGISTER_USER",           // Esperando que el usuario envíe su nombre
  REGISTER_CONFIRM = "REGISTER_CONFIRM",     // Confirmar datos ingresados

  // Usuario ya registrado (menú principal)
  MENU = "MENU",                             // Menú principal
  MENU_WAITING_OPTION = "MENU_WAITING_OPTION",
  CREATE_CARER = "CREATING_CARER",
  CREATE_MANUALLY_NOTIFICATION= "CREATING_MANUALLY_NOTIFICATION",
  CREATE_NOTIFICATION= "CREATING_NOTIFICATION",
  EDIT_DELETE_NOTIFICATION = "EDIT_DELETE_NOTIFICACTION",

  // Enviar recetas
  RECIPE_CHOOSE_METHOD = "RECIPE_CHOOSE_METHOD", // Elegir si enviar imagen o manual
  RECIPE_WAITING_IMAGE = "RECIPE_WAITING_IMAGE", // Emviar imagen
  RECIPE_WAITING_TEXT = "RECIPE_WAITING_TEXT",   // Enviar receta escrita manualmente

  // Confirmaciones
  RECIPE_CONFIRM = "RECIPE_CONFIRM",

  // Estados auxiliares
  UNKNOWN = "UNKNOWN",
}