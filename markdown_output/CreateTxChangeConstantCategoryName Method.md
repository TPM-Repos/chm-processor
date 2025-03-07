Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeConstantCategoryName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeConstantCategoryName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantCategory_
    The constant category to change.

_newName_
    The new name.

Glossary Item Box

Creates a transaction which, when committed, will change the specified constant category's name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeConstantCategoryName( _
       ByVal _constantCategory_ As [ProjectConstantCategory](topic4219.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constantCategory As [ProjectConstantCategory](topic4219.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeConstantCategoryName(constantCategory, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeConstantCategoryName( 
       [ProjectConstantCategory](topic4219.md) _constantCategory_ ,
       string _newName_
    )  
  
#### Parameters

 _constantCategory_
    The constant category to change.
_newName_
    The new name.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


