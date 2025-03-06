![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormMessageRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormMessageRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formMessage_
    The form message to change.

_newRule_
    The new rule to assign to the form message.

Glossary Item Box

Creates a transaction which, when committed, will change a form message's rule property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormMessageRule( _
       ByVal _formMessage_ As [ProjectMessage](topic4601.md), _
       ByVal _newRule_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim formMessage As [ProjectMessage](topic4601.md)
    Dim newRule As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormMessageRule(formMessage, newRule)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormMessageRule( 
       [ProjectMessage](topic4601.md) _formMessage_ ,
       string _newRule_
    )  
  
#### Parameters

 _formMessage_
    The form message to change.
_newRule_
    The new rule to assign to the form message.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


