Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteForm Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteForm Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete a form by the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteForm( _
       ByVal _form_ As [FormNavigationStep](topic10153.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [FormNavigationStep](topic10153.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteForm(form)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteForm( 
       [FormNavigationStep](topic10153.md) _form_
    )  
  
#### Parameters

 _form_
    The form to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


