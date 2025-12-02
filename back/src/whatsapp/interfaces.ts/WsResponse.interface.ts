export interface WhatsappResponse {
    object: string;
    entry:  Entry[];
}

export interface Entry {
    id:      string;
    changes: Change[];
}

export interface Change {
    value: Value;
    field: string;
}

export interface Value {
    messaging_product: string;
    metadata:          Metadata;
    contacts:          Contact[];
    messages:          Message[];
}

export interface Contact {
    profile: Profile;
    wa_id:   string;
}

export interface Profile {
    name: string;
}

export interface Message {
    from:      string;
    id:        string;
    timestamp: string;
    type:      string;
    image:     Image;
}

export interface Image {
    mime_type: string;
    sha256:    string;
    id:        string;
    url:       string;
}

export interface Metadata {
    display_phone_number: string;
    phone_number_id:      string;
}

export interface ImageUrlInfo{
  url: string,
  mime_type: string,
  sha256: string,
  file_size: number,
  id: string,
  messaging_product: string
}
