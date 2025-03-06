![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChildId Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6246.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md) : ChildId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique id of the child driven component to which the reference applies, if appropriate. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {DebugGetChildIdAsString()", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property ChildId As Nullable(Of Guid)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReadOnlyReleasedComponentReferenceDetails](topic6239.md)
    Dim value As Nullable(Of Guid)
     
    value = instance.ChildId  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {DebugGetChildIdAsString()", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Nullable<Guid> ChildId {get;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This value is only specified if the reference is to a driven component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md)   
[ReadOnlyReleasedComponentReferenceDetails Members](topic6240.md)

©2024 DriveWorks Ltd. All Rights Reserved.
