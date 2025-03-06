![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Example: Loading Defaults from a File in a Specification Flow Task   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2.md)  
  
Glossary Item Box

# Introduction

This example shows a specification flow task which will load defaults from a file called "Defaults.txt" which is placed in the same folder as the project.

To use this example, first create a Specification Flow Task Extension Library called "MyExtensionLibrary" using the project template installed into Visual Studio, and then replace the code in the Task1.vb file with the code below.

![](images/hs-tip.gif) | If you call your extension library something other than MyExtensionLibrary, you will need to change the line containing "embedded://" so that instead of saying MyExtensionLibrary, it contains your extension library's name.  
---|---  
  
# Example File

Defaults.txt | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    ControlName1=Default Value 1
    ControlName2=Default Value 2
    ControlName3=Default Value 3
      
  
# Specification Flow Code

MyExtender.vb | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    ' Import main DriveWorks types
    Imports DriveWorks
    
    ' Import the Specification namespace so we have access to Specification flow
    Imports DriveWorks.Specification
    
    <Task("My Task", "embedded://MyExtensionLibrary.Puzzle-16x16.png")> _
    Public Class MyTask
        Inherits Task
    
        Dim MyProperty As FlowProperty(Of String) = Me.Properties.RegisterStringProperty("File Name")
    
        Protected Overrides Sub Execute(ByVal ctx As SpecificationContext)
            Dim project = ctx.Project
    
            ' Get DriveWorks to figure out the full path to the file by just giving the file name
            ' and telling DriveWorks it's next to the project
            Dim fileName = project.Utility.ResolvePath(MyProperty.Value, RelativeToDirectory.Project)
            Dim fileLines = System.IO.File.ReadAllLines(fileName)
    
            For Each fileLine In fileLines
    
                ' Quick way to separate a line separated by an equals sign,
                ' NOTE: This will fail if there isn't an equals sign!
                Dim parts = fileLine.Split(New Char() {"="}, 2)
                Dim name = parts(0)
                Dim value = parts(1)
    
                Dim control = project.Navigation.GetControl(name)
    
                If control Is Nothing Then
                    Continue For
                End If
    
                control.SetInputValue(value)
            Next
        End Sub
    End Class
      
  

