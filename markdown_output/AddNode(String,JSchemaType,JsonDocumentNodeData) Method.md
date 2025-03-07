Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddNode(String,JSchemaType,JsonDocumentNodeData) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocument Class](topic3635.md) > [AddNode Method](topic3642.md) : AddNode(String,JSchemaType,JsonDocumentNodeData) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_schemaName_
    The schema name of the object.

_type_
    The data type tha this node represents.

_parent_
    The intended parent node of the node being created.

Glossary Item Box

Adds a new node to the documents structure. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddNode( _
       ByVal _schemaName_ As String, _
       ByVal _type_ As Newtonsoft.Json.Schema.JSchemaType, _
       ByVal _parent_ As [JsonDocumentNodeData](topic3659.md) _
    ) As [JsonDocumentNodeData](topic3659.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JsonDocument](topic3635.md)
    Dim schemaName As String
    Dim type As Newtonsoft.Json.Schema.JSchemaType
    Dim parent As [JsonDocumentNodeData](topic3659.md)
    Dim value As [JsonDocumentNodeData](topic3659.md)
     
    value = instance.AddNode(schemaName, type, parent)  
  
C#|   
---|---  
      
    
    public [JsonDocumentNodeData](topic3659.md) AddNode( 
       string _schemaName_ ,
       Newtonsoft.Json.Schema.JSchemaType _type_ ,
       [JsonDocumentNodeData](topic3659.md) _parent_
    )  
  
#### Parameters

 _schemaName_
    The schema name of the object.
_type_
    The data type tha this node represents.
_parent_
    The intended parent node of the node being created.

#### Return Value

The [JsonDocumentNodeData](topic3659.md) for the created node.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JsonDocument Class](topic3635.md)   
[JsonDocument Members](topic3636.md)   
[Overload List](topic3642.md)


