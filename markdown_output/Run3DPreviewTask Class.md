       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Run3DPreviewTask Class   
[Members](topic12513.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) : Run3DPreviewTask Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A specification-flow task for getting the 3d preview model for a preview control. 

# Object Model

![](dotnetdiagramimages/image674.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[TaskAttribute](topic11659.md)(DisplayName="resx://DriveWorks.TasksLocalizedResources,TaskDispNameRun3DPreview", 
       Image="embedded://DriveWorks.PictureBoxPlain16.png", 
       CategoryName="resx://DriveWorks.TasksLocalizedResources,TaskCategory3D", 
       WarningOutputEnabled=True)>
    Public Class Run3DPreviewTask 
       Inherits [DriveWorks.Specification.Task](topic11629.md)
       Implements [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Run3DPreviewTask](topic12512.md)  
  
C#|   
---|---  
      
    
    [[TaskAttribute](topic11659.md)(DisplayName="resx://DriveWorks.TasksLocalizedResources,TaskDispNameRun3DPreview", 
       Image="embedded://DriveWorks.PictureBoxPlain16.png", 
       CategoryName="resx://DriveWorks.TasksLocalizedResources,TaskCategory3D", 
       WarningOutputEnabled=true)]
    public class Run3DPreviewTask : [DriveWorks.Specification.Task](topic11629.md), [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md)  
[DriveWorks.Specification.Task](topic11629.md)  
**DriveWorks.Specification.StandardTasks.Run3DPreviewTask**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Run3DPreviewTask Members](topic12513.md)   
[DriveWorks.Specification.StandardTasks Namespace](topic11896.md)


