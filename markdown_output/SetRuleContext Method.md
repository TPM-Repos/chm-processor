       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRuleContext Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : SetRuleContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to set the context of.

_context_
    The context to give the rule.

Glossary Item Box

Sets a rule context that will be use by the Titan rule engine when evaluating the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub SetRuleContext( _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md), _
       ByVal _context_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim context As Object
     
    instance.SetRuleContext(rule, context)  
  
C#|   
---|---  
      
    
    protected void SetRuleContext( 
       [ProjectDocumentRule](topic4399.md) _rule_ ,
       object _context_
    )  
  
#### Parameters

 _rule_
    The rule to set the context of.
_context_
    The context to give the rule.

# Remarks

This is typically used to provide custom MyName() values, or relative rule resolvers.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)


