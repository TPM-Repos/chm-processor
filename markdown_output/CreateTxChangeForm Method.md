Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeForm Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeForm Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form to update.

_nextStep_
    The next step, from this form.

_left_
    The horrizontal position of the form.

_top_
    The vertical position of the form.

Glossary Item Box

Creates a transaction which, when committed, will update a form with the given name to the given properties, only project and name are needed 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeForm( _
       ByVal _form_ As [NavigationStep](topic10175.md), _
       ByVal _nextStep_ As [NavigationStep](topic10175.md), _
       ByVal _left_ As Integer, _
       ByVal _top_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [NavigationStep](topic10175.md)
    Dim nextStep As [NavigationStep](topic10175.md)
    Dim left As Integer
    Dim top As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeForm(form, nextStep, left, top)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeForm( 
       [NavigationStep](topic10175.md) _form_ ,
       [NavigationStep](topic10175.md) _nextStep_ ,
       int _left_ ,
       int _top_
    )  
  
#### Parameters

 _form_
    The form to update.
_nextStep_
    The next step, from this form.
_left_
    The horrizontal position of the form.
_top_
    The vertical position of the form.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


