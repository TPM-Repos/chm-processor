![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationDetails Class   
[Members](topic11293.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11292.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationDetails Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a registered DriveWorks specification. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image572.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    <KnownTypeAttribute(MethodName="", Type=System.String[])>
    <SerializableAttribute()>
    Public NotInheritable Class SpecificationDetails   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SpecificationDetails](topic11292.md)  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    [KnownTypeAttribute(MethodName="", Type=System.String[])]
    [SerializableAttribute()]
    public sealed class SpecificationDetails   
  
# ![](dotnetimages/collapse.gif)Remarks

Modifications made to an instance of SpecificationDetails are not immediately reflected in the group from which the instance was obtained. To apply any modifications, call the **DriveWorks.GroupSpecifications.TryUpdateSpecification** method.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
**DriveWorks.Specification.SpecificationDetails**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationDetails Members](topic11293.md)   
[DriveWorks.Specification Namespace](topic10764.md)

©2024 DriveWorks Ltd. All Rights Reserved.
