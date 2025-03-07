Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeParentVariableCategory(ProjectVariableCategory,ProjectVariableCategory) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeParentVariableCategory Method](topic12990.md) : CreateTxChangeParentVariableCategory(ProjectVariableCategory,ProjectVariableCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variableCategory_
    The variable category to modify.

_newParentCategory_
    The new parent category, or a null reference (Nothing in Visual Basic) to remove the parent.

Glossary Item Box

Creates a transaction which, when committed, will change the parent category of the specified variable category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeParentVariableCategory( _
       ByVal _variableCategory_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _newParentCategory_ As [ProjectVariableCategory](topic4983.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variableCategory As [ProjectVariableCategory](topic4983.md)
    Dim newParentCategory As [ProjectVariableCategory](topic4983.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeParentVariableCategory(variableCategory, newParentCategory)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeParentVariableCategory( 
       [ProjectVariableCategory](topic4983.md) _variableCategory_ ,
       [ProjectVariableCategory](topic4983.md) _newParentCategory_
    )  
  
#### Parameters

 _variableCategory_
    The variable category to modify.
_newParentCategory_
    The new parent category, or a null reference (Nothing in Visual Basic) to remove the parent.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12990.md)


