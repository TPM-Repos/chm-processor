Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeConstantCategoryImagePath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeConstantCategoryImagePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantCategory_
    The constant category to change.

_newImagePath_
    The new image path.

Glossary Item Box

Creates a transaction which, when committed, will change the specified constant category's image path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeConstantCategoryImagePath( _
       ByVal _constantCategory_ As [ProjectConstantCategory](topic4219.md), _
       ByVal _newImagePath_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constantCategory As [ProjectConstantCategory](topic4219.md)
    Dim newImagePath As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeConstantCategoryImagePath(constantCategory, newImagePath)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeConstantCategoryImagePath( 
       [ProjectConstantCategory](topic4219.md) _constantCategory_ ,
       string _newImagePath_
    )  
  
#### Parameters

 _constantCategory_
    The constant category to change.
_newImagePath_
    The new image path.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


