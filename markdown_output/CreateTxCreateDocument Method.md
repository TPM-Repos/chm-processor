Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_documentType_
    The type of the document to create, must be a subclass of [DriveWorks.ProjectDocument](topic4356.md).

_documentName_
    The name of the document to create.

Glossary Item Box

Creates a transaction which, when committed, will create a document of the specified type, with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateDocument( _
       ByVal _documentType_ As Type, _
       ByVal _documentName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim documentType As Type
    Dim documentName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateDocument(documentType, documentName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateDocument( 
       Type _documentType_ ,
       string _documentName_
    )  
  
#### Parameters

 _documentType_
    The type of the document to create, must be a subclass of [DriveWorks.ProjectDocument](topic4356.md).
_documentName_
    The name of the document to create.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


