       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Task Class   
[Members](topic11630.md) Example   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : Task Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The base class for all tasks which can be added to the task sequences for events which get fired by operations, transitions, and states. 

# Object Model

![](dotnetdiagramimages/image595.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class Task 
       Inherits [DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md)
       Implements [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Task](topic11629.md)  
  
C#|   
---|---  
      
    
    public abstract class Task : [DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md), [DriveWorks.EventFlow.IFlowNode](topic6873.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Example

Visual Basic| Copy Code  
---|---  
      
    
    ' Import main DriveWorks types
    Imports DriveWorks
     
    ' Import the Specification namespace so we have access to Specification flow
    Imports DriveWorks.Specification
     
    <Task("My Task", "embedded://MyTasksAndConditions3.Puzzle-16x16.png")> _
    Public Class MyTask
       Inherits Task
     
       ' Register properties so DriveWorks can see them and build rules for them
       Private mMyName As FlowProperty(Of String) = Me.Properties.RegisterStringProperty("Name", "Name of the constant to set")
       Private mMyValue As FlowProperty(Of String) = Me.Properties.RegisterStringProperty("Value", "Value of the constant")
     
       Protected Overrides Sub Execute(ByVal ctx As SpecificationContext)
           Dim theConstant As ProjectConstant = Nothing
     
           ' Perform the main work of the task here
           If ctx.Project.Constants.TryGetConstant(mMyName.Value, theConstant) Then
     
               ' Set the constant value 
               theConstant.Value = mMyValue.Value
           Else
     
               ' Report that we couldn't find the constant
               ctx.Report.WriteEntry(Reporting.ReportingLevel.Minimal, Reporting.ReportEntryType.Error, "My Task", "Constant: " & mMyName.Value, "The constant didn't exist", Nothing)
           End If
       End Sub
    End Class  
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
[DriveWorks.EventFlow.ExecutableNodeBase](topic6938.md)  
[DriveWorks.EventFlow.ExecutableNodeWithStatus](topic6990.md)  
**DriveWorks.Specification.Task**  
[DriveWorks.EventFlow.SubFlowInputsNode](topic7136.md)  
[DriveWorks.EventFlow.SubFlowOutputsNode](topic7143.md)  
[DriveWorks.Specification.StandardTasks.AddTeamTask](topic11905.md)  
[DriveWorks.Specification.StandardTasks.AddUserTask](topic11914.md)  
[DriveWorks.Specification.StandardTasks.AddUserToTeamTask](topic11930.md)  
[DriveWorks.Specification.StandardTasks.ArchiveSpecificationTask](topic11941.md)  
[DriveWorks.Specification.StandardTasks.Base64EncodeFileTask](topic11950.md)  
[DriveWorks.Specification.StandardTasks.CancelHostedSpecificationTask](topic11961.md)  
[DriveWorks.Specification.StandardTasks.CancelSpecificationTask](topic11971.md)  
[DriveWorks.Specification.StandardTasks.CancelSpecificationTimerTask](topic11979.md)  
[DriveWorks.Specification.StandardTasks.ChangeChildSpecificationStateTask](topic11988.md)  
[DriveWorks.Specification.StandardTasks.ClearComponentsDeferredFlagTask](topic12000.md)  
[DriveWorks.Specification.StandardTasks.ClearSpecificationComponentsDeferredFlagTask](topic12010.md)  
[DriveWorks.Specification.StandardTasks.ClickatellTask](topic12020.md)  
[DriveWorks.Specification.StandardTasks.CompleteChildSpecificationTask](topic12027.md)  
[DriveWorks.Specification.StandardTasks.CopyClosedChildSpecificationTask](topic12036.md)  
[DriveWorks.Specification.StandardTasks.CopyClosedSpecificationTask](topic12048.md)  
[DriveWorks.Specification.StandardTasks.CopyFileTask](topic12060.md)  
[DriveWorks.Specification.StandardTasks.CopyFolderTask](topic12072.md)  
[DriveWorks.Specification.StandardTasks.CopySpecificationTask](topic12084.md)  
[DriveWorks.Specification.StandardTasks.CreateClosedChildSpecificationTask](topic12094.md)  
[DriveWorks.Specification.StandardTasks.CreateProjectMetadataTask](topic12107.md)  
[DriveWorks.Specification.StandardTasks.DelayMacroTimeoutTask](topic12115.md)  
[DriveWorks.Specification.StandardTasks.DeleteCalculationTableRowsTask](topic12122.md)  
[DriveWorks.Specification.StandardTasks.DeleteFileTask](topic12134.md)  
[DriveWorks.Specification.StandardTasks.DeleteFolderTask](topic12143.md)  
[DriveWorks.Specification.StandardTasks.DeleteGroupTableRowsTask](topic12153.md)  
[DriveWorks.Specification.StandardTasks.DeleteSimpleTableRowsTask](topic12165.md)  
[DriveWorks.Specification.StandardTasks.DeleteSpecificationTask](topic12177.md)  
[DriveWorks.Specification.StandardTasks.DeleteTeamTask](topic12186.md)  
[DriveWorks.Specification.StandardTasks.DeleteUserTask](topic12196.md)  
[DriveWorks.Specification.StandardTasks.DesignMasterMacroLoopTask](topic12206.md)  
[DriveWorks.Specification.StandardTasks.DesignMasterMacroTask](topic12219.md)  
[DriveWorks.Specification.StandardTasks.DriveConstantValueTask](topic12232.md)  
[DriveWorks.Specification.StandardTasks.DriveControlValueTask](topic12245.md)  
[DriveWorks.Specification.StandardTasks.EvaluateRuleValueTask](topic12258.md)  
[DriveWorks.Specification.StandardTasks.ExportSpecificationDataTask](topic12270.md)  
[DriveWorks.Specification.StandardTasks.GetConstantValueTask](topic12283.md)  
[DriveWorks.Specification.StandardTasks.GetControlValueTask](topic12295.md)  
[DriveWorks.Specification.StandardTasks.IncrementRevisionNumberTask](topic12307.md)  
[DriveWorks.Specification.StandardTasks.InvokeChildSpecificationOperationTask](topic12317.md)  
[DriveWorks.Specification.StandardTasks.InvokeChildSpecificationTransitionTask](topic12330.md)  
[DriveWorks.Specification.StandardTasks.InvokeOperationOnExistingSpecificationTask](topic12343.md)  
[DriveWorks.Specification.StandardTasks.InvokeSpecificationOperationTask](topic12352.md)  
[DriveWorks.Specification.StandardTasks.InvokeSpecificationTransitionTask](topic12361.md)  
[DriveWorks.Specification.StandardTasks.InvokeTransitionOnExistingSpecificationTask](topic12370.md)  
[DriveWorks.Specification.StandardTasks.NavigateBackward](topic12379.md)  
[DriveWorks.Specification.StandardTasks.NavigateForward](topic12387.md)  
[DriveWorks.Specification.StandardTasks.ReadTextFileTask](topic12395.md)  
[DriveWorks.Specification.StandardTasks.RealTimeReleaseModelsTask](topic12405.md)  
[DriveWorks.Specification.StandardTasks.RefreshTableTask](topic12415.md)  
[DriveWorks.Specification.StandardTasks.RegenerateAndDeleteComponentTask](topic12426.md)  
[DriveWorks.Specification.StandardTasks.RegenerateAndDeleteSpecificationComponentsTask](topic12436.md)  
[DriveWorks.Specification.StandardTasks.RegenerateAndOverwriteComponentTask](topic12446.md)  
[DriveWorks.Specification.StandardTasks.RegenerateAndOverwriteSpecificationComponentsTask](topic12456.md)  
[DriveWorks.Specification.StandardTasks.ReleaseDocumentsTask](topic12466.md)  
[DriveWorks.Specification.StandardTasks.ReleaseEmailsTask](topic12477.md)  
[DriveWorks.Specification.StandardTasks.ReleaseModelsTask](topic12489.md)  
[DriveWorks.Specification.StandardTasks.RemoveUserFromTeamTask](topic12501.md)  
[DriveWorks.Specification.StandardTasks.Run3DPreviewTask](topic12512.md)  
[DriveWorks.Specification.StandardTasks.RunMacroInHostedSpecificationTask](topic12523.md)  
[DriveWorks.Specification.StandardTasks.RunMacroInHostSpecificationTask](topic12536.md)  
[DriveWorks.Specification.StandardTasks.SendHttpRequestTask](topic12548.md)  
[DriveWorks.Specification.StandardTasks.SetAllTeamsCanRunDriveAppTask](topic12557.md)  
[DriveWorks.Specification.StandardTasks.SetOwnerTask](topic12566.md)  
[DriveWorks.Specification.StandardTasks.SetProjectMetadataValueTask](topic12576.md)  
[DriveWorks.Specification.StandardTasks.SetSpecificationHostControlTask](topic12584.md)  
[DriveWorks.Specification.StandardTasks.SetStatesToTriggerOnTask](topic12600.md)  
[DriveWorks.Specification.StandardTasks.SetUserEnabledTask](topic12612.md)  
[DriveWorks.Specification.StandardTasks.SkipRemainingTasksTask](topic12623.md)  
[DriveWorks.Specification.StandardTasks.SkipToFormTask](topic12631.md)  
[DriveWorks.Specification.StandardTasks.StartAutopilotTask](topic12644.md)  
[DriveWorks.Specification.StandardTasks.StartChildSpecificationTask](topic12653.md)  
[DriveWorks.Specification.StandardTasks.StartSpecificationTimerTask](topic12661.md)  
[DriveWorks.Specification.StandardTasks.StopAutopilotTask](topic12676.md)  
[DriveWorks.Specification.StandardTasks.StoreSpecificationTask](topic12685.md)  
[DriveWorks.Specification.StandardTasks.UpdateFormUITask](topic12695.md)  
[DriveWorks.Specification.StandardTasks.UpdateGroupTableUsingArrayTask](topic12703.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamDisplayNameTask](topic12715.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamDriveAppPermissionsTask](topic12724.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamLeaderStatusTask](topic12733.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamMembersCanCaptureTask](topic12744.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamMembersCanEditAllSpecificationsTask](topic12753.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamMembersCanEditDriveAppsTask](topic12762.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamMembersCanEditGroupSecurityTask](topic12771.md)  
[DriveWorks.Specification.StandardTasks.UpdateTeamProjectPermissions](topic12780.md)  
[DriveWorks.Specification.StandardTasks.UpdateUserDisplayNameTask](topic12789.md)  
[DriveWorks.Specification.StandardTasks.UpdateUserEmailAddressTask](topic12800.md)  
[DriveWorks.Specification.StandardTasks.UpdateUserPasswordTask](topic12811.md)  
[DriveWorks.Specification.StandardTasks.ZipFolderTask](topic12822.md)  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Task Members](topic11630.md)   
[DriveWorks.Specification Namespace](topic10764.md)


