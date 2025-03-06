![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenericRule Constructor(String,String[],String,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [GenericRule Class](topic6043.md) > [GenericRule Constructor](topic6049.md) : GenericRule Constructor(String,String[],String,String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The display name of the rule.

_type_
    The type of the rule.

_formula_
    The formula which defines the rule.

_comment_
    The comment which describes the operation of the rule.

Glossary Item Box

Initializes a new instance of the [GenericRule](topic6043.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _displayName_ As String, _
       ByVal _type_() As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim type() As String
    Dim formula As String
    Dim comment As String
     
    Dim instance As New [GenericRule](topic6043.md)(displayName, type, formula, comment)  
  
C#|   
---|---  
      
    
    public GenericRule( 
       string _displayName_ ,
       string[] _type_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _displayName_
    The display name of the rule.
_type_
    The type of the rule.
_formula_
    The formula which defines the rule.
_comment_
    The comment which describes the operation of the rule.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenericRule Class](topic6043.md)   
[GenericRule Members](topic6044.md)   
[Overload List](topic6049.md)


