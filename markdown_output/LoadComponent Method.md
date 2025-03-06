![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadComponent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4112.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSet Class](topic4106.md) : LoadComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Loads the component from the component file. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function LoadComponent() As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSet](topic4106.md)
    Dim value As Boolean
     
    value = instance.LoadComponent()  
  
C#|   
---|---  
      
    
    public bool LoadComponent()  
  
#### Return Value

False if the component could not be loaded because the underlying capture data has been removed, i.e. the component has been uncaptured.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.NotSupportedException| No implementation of the component type was registered.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponentSet Class](topic4106.md)   
[ProjectComponentSet Members](topic4107.md)

©2024 DriveWorks Ltd. All Rights Reserved.
