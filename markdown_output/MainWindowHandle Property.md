Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MainWindowHandle Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplication Interface](topic24.md) : MainWindowHandle Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns the window handle of the main form of the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property MainWindowHandle As IntPtr  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplication](topic24.md)
    Dim value As IntPtr
     
    value = instance.MainWindowHandle  
  
C#|   
---|---  
      
    
    IntPtr MainWindowHandle {get;}  
  
#### Property Value

The window handle of the main window of the application if supported, otherwise .

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplication Interface](topic24.md)   
[IApplication Members](topic25.md)


