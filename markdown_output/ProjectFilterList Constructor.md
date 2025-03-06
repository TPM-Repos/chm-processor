![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectFilterList Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectFilterList Class](topic4470.md) : ProjectFilterList Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project to attach to.

_UISection_
    The unique section to attach to.

Glossary Item Box

Creates a new instance of the ProjectFilterList class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _project_ As [Project](topic3859.md), _
       ByVal _UISection_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim project As [Project](topic3859.md)
    Dim UISection As String
     
    Dim instance As New [ProjectFilterList](topic4470.md)(project, UISection)  
  
C#|   
---|---  
      
    
    public ProjectFilterList( 
       [Project](topic3859.md) _project_ ,
       string _UISection_
    )  
  
#### Parameters

 _project_
    The project to attach to.
_UISection_
    The unique section to attach to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectFilterList Class](topic4470.md)   
[ProjectFilterList Members](topic4471.md)


