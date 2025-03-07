Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeParentConstantCategory(ProjectConstant,ProjectConstantCategory) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeParentConstantCategory Method](topic12984.md) : CreateTxChangeParentConstantCategory(ProjectConstant,ProjectConstantCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constant_
    The constant to modify.

_newCategory_
    The new parent category, or a null reference (Nothing in Visual Basic) to remove the parent.

Glossary Item Box

Creates a transaction which, when committed, will change the parent category of the specified constant. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeParentConstantCategory( _
       ByVal _constant_ As [ProjectConstant](topic4171.md), _
       ByVal _newCategory_ As [ProjectConstantCategory](topic4219.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim constant As [ProjectConstant](topic4171.md)
    Dim newCategory As [ProjectConstantCategory](topic4219.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeParentConstantCategory(constant, newCategory)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeParentConstantCategory( 
       [ProjectConstant](topic4171.md) _constant_ ,
       [ProjectConstantCategory](topic4219.md) _newCategory_
    )  
  
#### Parameters

 _constant_
    The constant to modify.
_newCategory_
    The new parent category, or a null reference (Nothing in Visual Basic) to remove the parent.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12984.md)


