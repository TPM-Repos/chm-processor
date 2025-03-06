![](images/collapse.gif) ![](images/expand.gif) ![](images/copycode.gif) ![](images/copycodeHighlight.gif) ![](images/drpdown.gif) ![](images/drpdown_orange.gif)  
  
---  
DriveWorks SDK Documentation  |   
---|---  
Example: Loading Defaults from a File in a Macro   
[Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1.md)  
  
Glossary Item Box

# Introduction

This example shows a macro which will load defaults from a file called "Defaults.txt" which is placed in the same folder as the project.

To use this example, first create a Project Extender, and then copy the code below into your project extender class.

# Example File

Defaults.txt | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    ControlName1=Default Value 1
    ControlName2=Default Value 2
    ControlName3=Default Value 3
      
  
# Macro Code

MyExtender.vb | ![](images/copycode.gif)Copy Code  
---|---  
      
    
    <Macro()>
    Sub LoadDefaults()
    
        ' Get DriveWorks to figure out the full path to the file by just giving the file name
        ' and telling DriveWorks it's next to the project
        Dim fileName = Me.Project.Utility.ResolvePath("Defaults.txt", RelativeToDirectory.Project)
    
        ' Read the file
        Dim fileLines = System.IO.File.ReadAllLines(fileName)
    
        For Each fileLine In fileLines
    
            ' Quick way to separate a line separated by an equals sign,
            ' NOTE: This will fail if there isn't an equals sign!
            Dim parts = fileLine.Split(New Char() {"="}, 2)
            Dim name = parts(0)
            Dim value = parts(1)
    
            Dim control = Me.Project.Navigation.GetControl(name)
    
            If control Is Nothing Then
                Continue For
            End If
    
            control.SetInputValue(value)
        Next
    End Sub
      
  
©2024 DriveWorks Ltd. All Rights Reserved.
