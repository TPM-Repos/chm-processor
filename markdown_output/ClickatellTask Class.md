Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ClickatellTask Class   
[Members](topic12021.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) : ClickatellTask Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Sends a text message using the Clickatell service. 

# Object Model

![](dotnetdiagramimages/image628.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <[TaskAttribute](topic11659.md)(DisplayName="resx://DriveWorks.TasksLocalizedResources,SendTextClickatell", 
       Image="embedded://DriveWorks.ClickatellPlain16.png", 
       CategoryName="resx://DriveWorks.TasksLocalizedResources,TaskCategoryServices", 
       WarningOutputEnabled=False)>
    Public Class ClickatellTask 
       Inherits [DriveWorks.Specification.Task](topic11629.md)
       Implements [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ClickatellTask](topic12020.md)  
  
C#|   
---|---  
      
    
    [[TaskAttribute](topic11659.md)(DisplayName="resx://DriveWorks.TasksLocalizedResources,SendTextClickatell", 
       Image="embedded://DriveWorks.ClickatellPlain16.png", 
       CategoryName="resx://DriveWorks.TasksLocalizedResources,TaskCategoryServices", 
       WarningOutputEnabled=false)]
    public class ClickatellTask : [DriveWorks.Specification.Task](topic11629.md), [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md)  
[DriveWorks.Specification.Task](topic11629.md)  
**DriveWorks.Specification.StandardTasks.ClickatellTask**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ClickatellTask Members](topic12021.md)   
[DriveWorks.Specification.StandardTasks Namespace](topic11896.md)


