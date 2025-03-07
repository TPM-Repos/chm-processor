Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDocument(Type,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) > [CreateDocument Method](topic4440.md) : CreateDocument(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentType_
    The type of the document to add.

_name_
    The name of the document to add.

Glossary Item Box

Creates and adds a new document to the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateDocument( _
       ByVal _documentType_ As Type, _
       ByVal _name_ As String _
    ) As [ProjectDocument](topic4356.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim documentType As Type
    Dim name As String
    Dim value As [ProjectDocument](topic4356.md)
     
    value = instance.CreateDocument(documentType, name)  
  
C#|   
---|---  
      
    
    public [ProjectDocument](topic4356.md) CreateDocument( 
       Type _documentType_ ,
       string _name_
    )  
  
#### Parameters

 _documentType_
    The type of the document to add.
_name_
    The name of the document to add.

#### Return Value

The newly created document.

# Exceptions

Exception| Description  
---|---  
[ItemExistsException](topic3561.md)| A document with the given name already exists.  
System.ArgumentOutOfRangeException| The type specified in documentType does not inherit from [ProjectDocument](topic4356.md) or isn't defined in a extension library.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)   
[Overload List](topic4440.md)


