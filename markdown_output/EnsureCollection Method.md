![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureCollection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6441.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskAccessor Class](topic6429.md) : EnsureCollection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_location_
    The location of the task collection.

Glossary Item Box

Ensures that a task collection for the given location has been created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function EnsureCollection( _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ComponentTaskCollection](topic6466.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskAccessor](topic6429.md)
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ComponentTaskCollection](topic6466.md)
     
    value = instance.EnsureCollection(location)  
  
C#|   
---|---  
      
    
    protected abstract [ComponentTaskCollection](topic6466.md) EnsureCollection( 
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    )  
  
#### Parameters

 _location_
    The location of the task collection.

#### Return Value

A task collection for the given location.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskAccessor Class](topic6429.md)   
[ComponentTaskAccessor Members](topic6430.md)

©2024 DriveWorks Ltd. All Rights Reserved.
