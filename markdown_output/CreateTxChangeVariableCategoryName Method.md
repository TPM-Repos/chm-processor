Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeVariableCategoryName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeVariableCategoryName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variableCategory_
    The variable category to change.

_newName_
    The new name.

Glossary Item Box

Creates a transaction which, when committed, will change the specified variable category's name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeVariableCategoryName( _
       ByVal _variableCategory_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variableCategory As [ProjectVariableCategory](topic4983.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeVariableCategoryName(variableCategory, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeVariableCategoryName( 
       [ProjectVariableCategory](topic4983.md) _variableCategory_ ,
       string _newName_
    )  
  
#### Parameters

 _variableCategory_
    The variable category to change.
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


