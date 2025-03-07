Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateVariableCategory(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateVariableCategory Method](topic13077.md) : CreateTxCreateVariableCategory(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the new category.

_parentCategoryPath_
    Optionally, the parent category path, or a null reference to leave the category rooted.

Glossary Item Box

Creates a transaction which, when committed, will create a new variable category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateVariableCategory( _
       ByVal _displayName_ As String, _
       ByVal _parentCategoryPath_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim displayName As String
    Dim parentCategoryPath As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateVariableCategory(displayName, parentCategoryPath)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateVariableCategory( 
       string _displayName_ ,
       string _parentCategoryPath_
    )  
  
#### Parameters

 _displayName_
    The display name of the new category.
_parentCategoryPath_
    Optionally, the parent category path, or a null reference to leave the category rooted.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13077.md)


