Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateFormMessage Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateFormMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_code_
    The code to assign the new form message

_comment_
    

_rule_
    

Glossary Item Box

Creates a transaction which, when committed, will creates a form message with the given code number. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateFormMessage( _
       ByVal _code_ As Integer, _
       ByVal _comment_ As String, _
       ByVal _rule_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim code As Integer
    Dim comment As String
    Dim rule As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateFormMessage(code, comment, rule)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateFormMessage( 
       int _code_ ,
       string _comment_ ,
       string _rule_
    )  
  
#### Parameters

 _code_
    The code to assign the new form message
 _comment_
    
_rule_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


