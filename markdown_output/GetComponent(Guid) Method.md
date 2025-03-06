![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetComponent(Guid) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3037.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [GetComponent Method](topic3036.md) : GetComponent(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The unique identifier of the component.

Glossary Item Box

Gets the captured component with the specified identifier. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetComponent( _
       ByVal _componentId_ As Guid _
    ) As [CapturedComponent](topic6147.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim componentId As Guid
    Dim value As [CapturedComponent](topic6147.md)
     
    value = instance.GetComponent(componentId)  
  
C#|   
---|---  
      
    
    public [CapturedComponent](topic6147.md) GetComponent( 
       Guid _componentId_
    )  
  
#### Parameters

 _componentId_
    The unique identifier of the component.

#### Return Value

The component with the specified identifier if it is registered, otherwise a null reference.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The component type is not supported.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3036.md)

©2024 DriveWorks Ltd. All Rights Reserved.
