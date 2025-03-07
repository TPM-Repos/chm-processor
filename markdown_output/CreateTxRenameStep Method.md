Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRenameStep Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRenameStep Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_navStep_
    The form to delete.

_newName_
    

Glossary Item Box

Creates a transaction which, when committed, will delete a form by the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRenameStep( _
       ByVal _navStep_ As [NavigationStep](topic10175.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim navStep As [NavigationStep](topic10175.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRenameStep(navStep, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRenameStep( 
       [NavigationStep](topic10175.md) _navStep_ ,
       string _newName_
    )  
  
#### Parameters

 _navStep_
    The form to delete.
_newName_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


