![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProhibitedStatesAttribute Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ProhibitedStatesAttribute Class](topic13875.md) : ProhibitedStatesAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_states_
    The list of application states where this entity should not be visible.

Glossary Item Box

Creates a new instance of the [ProhibitedStatesAttribute](topic13875.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal ParamArray _states_() As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim states() As String
     
    Dim instance As New [ProhibitedStatesAttribute](topic13875.md)(states)  
  
C#|   
---|---  
      
    
    public ProhibitedStatesAttribute( 
       params string[] _states_
    )  
  
#### Parameters

 _states_
    The list of application states where this entity should not be visible.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProhibitedStatesAttribute Class](topic13875.md)   
[ProhibitedStatesAttribute Members](topic13876.md)


