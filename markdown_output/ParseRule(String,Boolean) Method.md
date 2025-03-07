Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ParseRule(String,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) > [ParseRule Method](topic4917.md) : ParseRule(String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleText_
    The rule to be parsed.

_includeFunctionCallsInReferences_
    True to include function calls in the resulting collection of references, otherwise false.

Glossary Item Box

Parses the specified rule into an instance of [DriveWorks.Rules.IRuleNode](topic10542.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ParseRule( _
       ByVal _ruleText_ As String, _
       ByVal _includeFunctionCallsInReferences_ As Boolean _
    ) As [IParseResult](topic10526.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim ruleText As String
    Dim includeFunctionCallsInReferences As Boolean
    Dim value As [IParseResult](topic10526.md)
     
    value = instance.ParseRule(ruleText, includeFunctionCallsInReferences)  
  
C#|   
---|---  
      
    
    public [IParseResult](topic10526.md) ParseRule( 
       string _ruleText_ ,
       bool _includeFunctionCallsInReferences_
    )  
  
#### Parameters

 _ruleText_
    The rule to be parsed.
_includeFunctionCallsInReferences_
    True to include function calls in the resulting collection of references, otherwise false.

#### Return Value

The parse result.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)   
[Overload List](topic4917.md)


