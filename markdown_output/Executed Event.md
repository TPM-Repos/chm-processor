Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Executed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [FlowBase Class](topic6999.md) : Executed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when this flow has been executed and can no longer be edited. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Executed As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FlowBase](topic6999.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.Executed, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> Executed  
  
# Remarks

You can reset the execution of this flow by calling Microsoft.VisualBasic.FileSystem.Reset.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FlowBase Class](topic6999.md)   
[FlowBase Members](topic7000.md)


