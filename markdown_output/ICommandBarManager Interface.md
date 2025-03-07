Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ICommandBarManager Interface   
[Members](topic110.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ICommandBarManager Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for an object which manages an application's command bar. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface ICommandBarManager 
       Inherits [IUpdateable](topic519.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandBarManager](topic109.md)  
  
C#|   
---|---  
      
    
    public interface ICommandBarManager : [IUpdateable](topic519.md)    
  
# Remarks

If a view wishes to create a command button group, it should use the [ViewControl.CommandBarManager](topic1142.md) property to access a [IViewCommandBarManager](topic543.md) rather than using this interface.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandBarManager Members](topic110.md)   
[DriveWorks.Applications Namespace](topic16.md)


