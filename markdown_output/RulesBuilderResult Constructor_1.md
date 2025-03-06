RulesBuilderResult Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [RulesBuilderResult Class](topic1622.md) : RulesBuilderResult Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_cancel_
    True if the rules builder was cancelled, otherwise false.

_rule_
    The rule that the user entered.

_comment_
    The comment that the user entered.

Glossary Item Box

Initializes a new instance of the [RulesBuilderResult](topic1622.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _cancel_ As Boolean, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim cancel As Boolean
    Dim rule As String
    Dim comment As String
     
    Dim instance As New [RulesBuilderResult](topic1622.md)(cancel, rule, comment)  
  
C#|   
---|---  
      
    
    public RulesBuilderResult( 
       bool _cancel_ ,
       string _rule_ ,
       string _comment_
    )  
  
#### Parameters

 _cancel_
    True if the rules builder was cancelled, otherwise false.
_rule_
    The rule that the user entered.
_comment_
    The comment that the user entered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RulesBuilderResult Class](topic1622.md)   
[RulesBuilderResult Members](topic1623.md)


