_TDocument_
    The type of the document to add.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDocument<TDocument>(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocuments Class](topic4434.md) > [CreateDocument Method](topic4440.md) : CreateDocument<TDocument>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the document to add.

Glossary Item Box

Creates and adds a new document to the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateDocument(Of TDocument As [ProjectDocument](topic4356.md))( _
       ByVal _name_ As String _
    ) As TDocument  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocuments](topic4434.md)
    Dim name As String
    Dim value As TDocument
     
    value = instance.CreateDocument(Of TDocument)(name)  
  
C#|   
---|---  
      
    
    public TDocument CreateDocument<TDocument>( 
       string _name_
    )
    where TDocument: [ProjectDocument](topic4356.md)  
  
#### Parameters

 _name_
    The name of the document to add.

#### Type Parameters

_TDocument_
    The type of the document to add.

#### Return Value

The newly created document.

# Exceptions

Exception| Description  
---|---  
[ItemExistsException](topic3561.md)| A document with the given name already exists.  
System.ArgumentOutOfRangeException| The specified type does not inherit from [ProjectDocument](topic4356.md).  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocuments Class](topic4434.md)   
[ProjectDocuments Members](topic4435.md)   
[Overload List](topic4440.md)


