Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeParentVariableCategory(ProjectVariable,ProjectVariableCategory) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeParentVariableCategory Method](topic12990.md) : CreateTxChangeParentVariableCategory(ProjectVariable,ProjectVariableCategory) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    The variable to modify.

_newCategory_
    The new parent category, or a null reference (Nothing in Visual Basic) to remove the parent.

Glossary Item Box

Creates a transaction which, when committed, will change the parent category of the specified variable. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeParentVariableCategory( _
       ByVal _variable_ As [ProjectVariable](topic4927.md), _
       ByVal _newCategory_ As [ProjectVariableCategory](topic4983.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variable As [ProjectVariable](topic4927.md)
    Dim newCategory As [ProjectVariableCategory](topic4983.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeParentVariableCategory(variable, newCategory)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeParentVariableCategory( 
       [ProjectVariable](topic4927.md) _variable_ ,
       [ProjectVariableCategory](topic4983.md) _newCategory_
    )  
  
#### Parameters

 _variable_
    The variable to modify.
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
[Overload List](topic12990.md)


