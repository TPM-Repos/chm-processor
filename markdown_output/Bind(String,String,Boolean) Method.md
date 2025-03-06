![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Bind(String,String,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperty Class](topic10946.md) > [Bind Method](topic10952.md) : Bind(String,String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to apply.

_comment_
    The comment to apply.

_allowEmptyRule_
    

Glossary Item Box

Binds the property to a rule. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Bind( _
       ByVal _rule_ As String, _
       ByVal _comment_ As String, _
       ByVal _allowEmptyRule_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FlowProperty](topic10946.md)
    Dim rule As String
    Dim comment As String
    Dim allowEmptyRule As Boolean
     
    instance.Bind(rule, comment, allowEmptyRule)  
  
C#|   
---|---  
      
    
    public void Bind( 
       string _rule_ ,
       string _comment_ ,
       bool _allowEmptyRule_
    )  
  
#### Parameters

 _rule_
    The rule to apply.
_comment_
    The comment to apply.
_allowEmptyRule_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowProperty Class](topic10946.md)   
[FlowProperty Members](topic10947.md)   
[Overload List](topic10952.md)


