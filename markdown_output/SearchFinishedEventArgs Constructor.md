![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SearchFinishedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10323.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [SearchFinishedEventArgs Class](topic10317.md) : SearchFinishedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_names_
    The names we searched for.

_uses_
    All uses in rules of the name we searched for.

Glossary Item Box

Initializes a new instance of the [SearchFinishedEventArgs](topic10317.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _names_() As String, _
       ByVal _uses_() As [RuleSearchResult](topic13227.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim names() As String
    Dim uses() As [RuleSearchResult](topic13227.md)
     
    Dim instance As New [SearchFinishedEventArgs](topic10317.md)(names, uses)  
  
C#|   
---|---  
      
    
    public SearchFinishedEventArgs( 
       string[] _names_ ,
       [RuleSearchResult](topic13227.md)[] _uses_
    )  
  
#### Parameters

 _names_
    The names we searched for.
_uses_
    All uses in rules of the name we searched for.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SearchFinishedEventArgs Class](topic10317.md)   
[SearchFinishedEventArgs Members](topic10318.md)

©2024 DriveWorks Ltd. All Rights Reserved.
