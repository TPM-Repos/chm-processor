![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DiagnosticPreparationInteraction Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified Namespace](topic15343.md) > [DiagnosticPreparationInteraction Class](topic15345.md) : DiagnosticPreparationInteraction Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dispatcher_
    The dispatcher marshalling the main thread.

_displayManager_
    

Glossary Item Box

Instantiates a new [DiagnosticPreparationInteraction](topic15345.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _dispatcher_ As Dispatcher, _
       ByVal _displayManager_ As DriveWorks.Applications.Implementation.Configuration.UIDisplayManager _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim dispatcher As Dispatcher
    Dim displayManager As DriveWorks.Applications.Implementation.Configuration.UIDisplayManager
     
    Dim instance As New [DiagnosticPreparationInteraction](topic15345.md)(dispatcher, displayManager)  
  
C#|   
---|---  
      
    
    public DiagnosticPreparationInteraction( 
       Dispatcher _dispatcher_ ,
       DriveWorks.Applications.Implementation.Configuration.UIDisplayManager _displayManager_
    )  
  
#### Parameters

 _dispatcher_
    The dispatcher marshalling the main thread.
_displayManager_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DiagnosticPreparationInteraction Class](topic15345.md)   
[DiagnosticPreparationInteraction Members](topic15346.md)


