Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeVariableRuleAndComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeVariableRuleAndComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    The variable to change.

_newRule_
    The new rule.

_newComment_
    The new comment.

Glossary Item Box

Creates a transaction which, when committed, will 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeVariableRuleAndComment( _
       ByVal _variable_ As [ProjectVariable](topic4927.md), _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim variable As [ProjectVariable](topic4927.md)
    Dim newRule As String
    Dim newComment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeVariableRuleAndComment(variable, newRule, newComment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeVariableRuleAndComment( 
       [ProjectVariable](topic4927.md) _variable_ ,
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _variable_
    The variable to change.
_newRule_
    The new rule.
_newComment_
    The new comment.

#### Return Value

A transaction which, when executed, will perform the operation.

# Remarks

This transaction should be used when changing rules and comments to make sure that rule history is not duplicated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


