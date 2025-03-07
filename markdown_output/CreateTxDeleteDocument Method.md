Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteDocument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteDocument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_document_
    The document to be deleted.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteDocument( _
       ByVal _document_ As [ProjectDocument](topic4356.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim document As [ProjectDocument](topic4356.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteDocument(document)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteDocument( 
       [ProjectDocument](topic4356.md) _document_
    )  
  
#### Parameters

 _document_
    The document to be deleted.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


