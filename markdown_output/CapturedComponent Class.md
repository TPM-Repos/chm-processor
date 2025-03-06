![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CapturedComponent Class   
[Members](topic6148.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6147.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : CapturedComponent Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides the base class for captured components, which should be implemented by a component provider. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image315.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class CapturedComponent 
       Inherits DriveWorks.DomainObject  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedComponent](topic6147.md)  
  
C#|   
---|---  
      
    
    public abstract class CapturedComponent : DriveWorks.DomainObject   
  
# ![](dotnetimages/collapse.gif)Remarks

When retrieving a component from DriveWorks, you will need to cast from the `CapturedComponent` base type to the specific type of component you are dealing with, for example: `' Import the component namespace from DriveWorks.Engine.dll Imports DriveWorks.Components ' Import the SolidWorks specific namespace from DriveWorks.SolidWorks.dll Imports DriveWorks.Components ... Public Sub LoadComponent(ByVal group As Group, ByVal componentId As Guid) Dim myComponent As CapturedComponent = group.CapturedComponents.GetComponent(componentId) If TypeOf myComponent Is DriveWorks.SolidWorks.CapturedAssembly Then DoSomethingWithAssembly(DirectCast(myComponent, DriveWorks.SolidWorks.ProjectAssembly)) ElseIf TypeOf myComponent Is DriveWorks.SolidWorks.CapturedPart Then DoSomethingWithPart(DirectCast(myComponent, DriveWorks.SolidWorks.ProjectPart)) ElseIf TypeOf myComponent Is DriveWorks.SolidWorks.CapturedDrawing Then DoSomethingWithDrawing(DirectCast(myComponent, DriveWorks.SolidWorks.ProjectDrawing)) Else MessageBox.Show("Not a SolidWorks component.") End If End Sub`

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
**DriveWorks.Components.CapturedComponent**  
[DriveWorks.SolidWorks.Components.CapturedSolidWorksComponent](topic14343.md)  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedComponent Members](topic6148.md)   
[DriveWorks.Components Namespace](topic6089.md)

©2024 DriveWorks Ltd. All Rights Reserved.
