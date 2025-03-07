Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
JsonDocumentNodeData Constructor(JsonDocument,XElement,JsonDocumentNodeData)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JsonDocumentNodeData Class](topic3659.md) > [JsonDocumentNodeData Constructor](topic3665.md) : JsonDocumentNodeData Constructor(JsonDocument,XElement,JsonDocumentNodeData)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_document_
    The [JsonDocument](topic3635.md) associated with this node.

_originalElement_
    The original System.Xml.Linq.XElement associated with this Json Document Node from the document data.

_parent_
    A reference to the parent node. Passing Nothing will add this node to the root of the document.

Glossary Item Box

Creates a new instance of the [JsonDocumentNodeData](topic3659.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _document_ As [JsonDocument](topic3635.md), _
       ByVal _originalElement_ As XElement, _
       ByVal _parent_ As [JsonDocumentNodeData](topic3659.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim document As [JsonDocument](topic3635.md)
    Dim originalElement As XElement
    Dim parent As [JsonDocumentNodeData](topic3659.md)
     
    Dim instance As New [JsonDocumentNodeData](topic3659.md)(document, originalElement, parent)  
  
C#|   
---|---  
      
    
    public JsonDocumentNodeData( 
       [JsonDocument](topic3635.md) _document_ ,
       XElement _originalElement_ ,
       [JsonDocumentNodeData](topic3659.md) _parent_
    )  
  
#### Parameters

 _document_
    The [JsonDocument](topic3635.md) associated with this node.
_originalElement_
    The original System.Xml.Linq.XElement associated with this Json Document Node from the document data.
_parent_
    A reference to the parent node. Passing Nothing will add this node to the root of the document.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JsonDocumentNodeData Class](topic3659.md)   
[JsonDocumentNodeData Members](topic3660.md)   
[Overload List](topic3665.md)


