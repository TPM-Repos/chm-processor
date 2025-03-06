       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleChangeData Constructor(String,String,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RuleChangeData Class](topic5254.md) > [RuleChangeData Constructor](topic5260.md) : RuleChangeData Constructor(String,String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleName_
    The name of the rule.

_formula_
    The formula to apply to the rule.

_comment_
    The comment to apply to the rule.

Glossary Item Box

Creates a new instance of the [RuleChangeData](topic5254.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _ruleName_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim ruleName As String
    Dim formula As String
    Dim comment As String
     
    Dim instance As New [RuleChangeData](topic5254.md)(ruleName, formula, comment)  
  
C#|   
---|---  
      
    
    public RuleChangeData( 
       string _ruleName_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _ruleName_
    The name of the rule.
_formula_
    The formula to apply to the rule.
_comment_
    The comment to apply to the rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleChangeData Class](topic5254.md)   
[RuleChangeData Members](topic5255.md)   
[Overload List](topic5260.md)


