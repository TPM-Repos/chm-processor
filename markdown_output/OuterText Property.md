Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OuterText Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Rules Namespace](topic10510.md) > [IRuleNode Interface](topic10542.md) : OuterText Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The outer text value for this node. Same as [RuleText](topic10553.md), but formatted with ideal white spaces. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property OuterText As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IRuleNode](topic10542.md)
    Dim value As String
     
    value = instance.OuterText  
  
C#|   
---|---  
      
    
    string OuterText {get;}  
  
# Remarks

The outer text is the text of the node including its arguments, for example the outer text for an operator would be the left hand side, operator, and right hand side, and for an IF statement it would be the entire IF statement.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IRuleNode Interface](topic10542.md)   
[IRuleNode Members](topic10543.md)


