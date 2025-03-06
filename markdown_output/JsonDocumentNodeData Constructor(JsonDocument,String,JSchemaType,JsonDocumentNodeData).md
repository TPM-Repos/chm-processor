![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
JsonDocumentNodeData Constructor(JsonDocument,String,JSchemaType,JsonDocumentNodeData)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocumentNodeData Class](topic3659.md) > [JsonDocumentNodeData Constructor](topic3665.md) : JsonDocumentNodeData Constructor(JsonDocument,String,JSchemaType,JsonDocumentNodeData)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_document_
    The [JsonDocument](topic3635.md) associated with this node.

_schemaName_
    The name used to identify the schema definition in the documents Json Schema.

_type_
    The data type of the token that this node will hold.

_parent_
    A reference to the parent node. Passing Nothing will add this node to the root of the document.

Glossary Item Box

Creates a new instance of the [JsonDocumentNodeData](topic3659.md) class which is not yet been committed to the documents project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _document_ As [JsonDocument](topic3635.md), _
       ByVal _schemaName_ As String, _
       ByVal _type_ As Newtonsoft.Json.Schema.JSchemaType, _
       ByVal _parent_ As [JsonDocumentNodeData](topic3659.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim document As [JsonDocument](topic3635.md)
    Dim schemaName As String
    Dim type As Newtonsoft.Json.Schema.JSchemaType
    Dim parent As [JsonDocumentNodeData](topic3659.md)
     
    Dim instance As New [JsonDocumentNodeData](topic3659.md)(document, schemaName, type, parent)  
  
C#|   
---|---  
      
    
    public JsonDocumentNodeData( 
       [JsonDocument](topic3635.md) _document_ ,
       string _schemaName_ ,
       Newtonsoft.Json.Schema.JSchemaType _type_ ,
       [JsonDocumentNodeData](topic3659.md) _parent_
    )  
  
#### Parameters

 _document_
    The [JsonDocument](topic3635.md) associated with this node.
_schemaName_
    The name used to identify the schema definition in the documents Json Schema.
_type_
    The data type of the token that this node will hold.
_parent_
    A reference to the parent node. Passing Nothing will add this node to the root of the document.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JsonDocumentNodeData Class](topic3659.md)   
[JsonDocumentNodeData Members](topic3660.md)   
[Overload List](topic3665.md)


