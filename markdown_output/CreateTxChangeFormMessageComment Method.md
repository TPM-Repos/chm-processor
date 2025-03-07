Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormMessageComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormMessageComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_formMessage_
    The form message to change.

_newComment_
    The new comment to assign to the form message.

Glossary Item Box

Creates a transaction which, when committed, will change a form message's comment property. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormMessageComment( _
       ByVal _formMessage_ As [ProjectMessage](topic4601.md), _
       ByVal _newComment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim formMessage As [ProjectMessage](topic4601.md)
    Dim newComment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormMessageComment(formMessage, newComment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormMessageComment( 
       [ProjectMessage](topic4601.md) _formMessage_ ,
       string _newComment_
    )  
  
#### Parameters

 _formMessage_
    The form message to change.
_newComment_
    The new comment to assign to the form message.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


