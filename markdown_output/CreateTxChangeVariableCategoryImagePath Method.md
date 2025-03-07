Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeVariableCategoryImagePath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeVariableCategoryImagePath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variableCategory_
    The variable category to change.

_newImagePath_
    The new image path.

Glossary Item Box

Creates a transaction which, when committed, will change the specified variable category's image path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeVariableCategoryImagePath( _
       ByVal _variableCategory_ As [ProjectVariableCategory](topic4983.md), _
       ByVal _newImagePath_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variableCategory As [ProjectVariableCategory](topic4983.md)
    Dim newImagePath As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeVariableCategoryImagePath(variableCategory, newImagePath)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeVariableCategoryImagePath( 
       [ProjectVariableCategory](topic4983.md) _variableCategory_ ,
       string _newImagePath_
    )  
  
#### Parameters

 _variableCategory_
    The variable category to change.
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


