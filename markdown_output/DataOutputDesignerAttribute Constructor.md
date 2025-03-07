Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataOutputDesignerAttribute Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.Documents Namespace](topic1507.md) > [DataOutputDesignerAttribute Class](topic1546.md) : DataOutputDesignerAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentType_
    The type of document supported by the designer (must be derived from [DriveWorks.ProjectDocument](topic4356.md)).

_displayName_
    The localizable display name of the document type.

_image_
    The localizable image of the document type.

_descriptionHtml_
    The localizable description of the document.

Glossary Item Box

Initializes a new instance of the [DataOutputDesignerAttribute](topic1546.md) attribute class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _documentType_ As Type, _
       ByVal _displayName_ As String, _
       ByVal _image_ As String, _
       ByVal _descriptionHtml_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim documentType As Type
    Dim displayName As String
    Dim image As String
    Dim descriptionHtml As String
     
    Dim instance As New [DataOutputDesignerAttribute](topic1546.md)(documentType, displayName, image, descriptionHtml)  
  
C#|   
---|---  
      
    
    public DataOutputDesignerAttribute( 
       Type _documentType_ ,
       string _displayName_ ,
       string _image_ ,
       string _descriptionHtml_
    )  
  
#### Parameters

 _documentType_
    The type of document supported by the designer (must be derived from [DriveWorks.ProjectDocument](topic4356.md)).
_displayName_
    The localizable display name of the document type.
_image_
    The localizable image of the document type.
_descriptionHtml_
    The localizable description of the document.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataOutputDesignerAttribute Class](topic1546.md)   
[DataOutputDesignerAttribute Members](topic1547.md)


