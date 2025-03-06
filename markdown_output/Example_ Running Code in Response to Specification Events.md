![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Example: Running Code in Response to Specification Events   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3.md)  
  
Glossary Item Box

# Introduction

This example shows how you can run code whenever certain events occur related to specifications.

There are lots of [events on the SpecificationContext](topic11149.md) that you can handle to run code at different times.

![](images/hs-tip.gif) |  Specification Context is an important class in DriveWorks. Specification Contexts are created by DriveWorks whenever it needs to work with a specification, not just for running a specification. This means, for example, that merely clicking on a specification in the Specification Explorer will result in a Specification Context being created so that DriveWorks can properly evaluate which operations and transitions are valid for that specification. This means that it is important not to perform any sort of expensive operations when a Specification Context is created - instead, handle the specific events on the Specification Context that you are interested in, and do your processing there.  
---|---  
  
# Example

Specification Events | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    Imports DriveWorks.Applications.Extensibility
    Imports DriveWorks.Applications
    Imports DriveWorks.Specification
    Imports System.Windows.Forms
    
    <ApplicationPlugin("SpecificationPluginExample", "Specification Plugin Example", "Illustrates the use of Specification Events")>
    Public Class SpecificationPluginExample
        Implements IApplicationPlugin
    
        ' Using WithEvents in VB makes it really easy to work with events
        Private WithEvents mSpecificationService As ISpecificationService
    
        Public Sub Initialize(application As DriveWorks.Applications.IApplication) Implements DriveWorks.Applications.Extensibility.IApplicationPlugin.Initialize
    
            ' Get the specification service from the DriveWorks Application
            mSpecificationService = application.ServiceManager.GetService(Of ISpecificationService)()
    
            ' DriveWorks may return Nothing if the application we're running in doesn't support
            ' working with specifications
            If mSpecificationService Is Nothing Then
                Return
            End If
        End Sub
    
        Private Sub mSpecificationService_SpecificationContextCreated(sender As Object, e As DriveWorks.Specification.SpecificationContextEventArgs) Handles mSpecificationService.SpecificationContextCreated
    
            ' Lots of specification contexts might be around at the same time, so create an object
            ' to handle each one
            Dim handler As New SpecificationHandler(e.Context)
        End Sub
    End Class
    
    Class SpecificationHandler
        Private WithEvents mSpecification As SpecificationContext
    
        Public Sub New(ByVal ctx As SpecificationContext)
            mSpecification = ctx
        End Sub
    
        Private Sub mSpecification_StartRequested(sender As Object, e As DriveWorks.Specification.ProjectDetailsEventArgs) Handles mSpecification.StartRequested
    
            ' This is an example of one event which you can handle, there are many events on the specification context
            ' that you can use to run code at different times
        End Sub
    End Class
      
  
©2024 DriveWorks Ltd. All Rights Reserved.
